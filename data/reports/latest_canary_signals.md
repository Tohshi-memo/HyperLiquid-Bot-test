# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T18:07:27.213662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.0191` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `0.0219` n `102`; fx avg `0.0053` n `6`; index avg `0.002` n `25`; metal avg `0.0097` n `20`; unknown avg `-0.0223` n `782`
- 1h: commodity avg `-0.0808` n `12`; crypto_alt avg `0.0926` n `230`; crypto_major avg `0.1844` n `8`; equity avg `0.0101` n `102`; fx avg `0.0067` n `6`; index avg `-0.0047` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0191` n `782`
- 4h: commodity avg `-0.1165` n `12`; crypto_alt avg `0.2492` n `230`; crypto_major avg `0.6009` n `8`; equity avg `0.3602` n `102`; fx avg `-0.0053` n `6`; index avg `0.0556` n `25`; metal avg `0.0684` n `20`; unknown avg `1.338` n `782`
- 24h: commodity avg `-1.3203` n `12`; crypto_alt avg `0.8357` n `230`; crypto_major avg `1.1494` n `8`; equity avg `1.3822` n `102`; fx avg `-0.1249` n `6`; index avg `0.2996` n `25`; metal avg `0.3336` n `20`; unknown avg `1.5441` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
