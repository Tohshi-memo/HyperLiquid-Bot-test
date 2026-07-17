# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T13:07:31.184950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1785` n `12`; crypto_alt avg `-0.7303` n `230`; crypto_major avg `-0.5806` n `8`; equity avg `-0.1927` n `96`; fx avg `0.0085` n `6`; index avg `-0.0495` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0016` n `769`
- 1h: commodity avg `0.1795` n `12`; crypto_alt avg `-0.9497` n `230`; crypto_major avg `-0.9202` n `8`; equity avg `-0.5419` n `96`; fx avg `0.0095` n `6`; index avg `-0.0805` n `25`; metal avg `-0.0785` n `20`; unknown avg `0.0364` n `769`
- 4h: commodity avg `0.3799` n `12`; crypto_alt avg `-0.8141` n `230`; crypto_major avg `-0.6684` n `8`; equity avg `0.1572` n `96`; fx avg `-0.0126` n `6`; index avg `0.0114` n `25`; metal avg `-0.1885` n `20`; unknown avg `0.0996` n `768`
- 24h: commodity avg `0.0841` n `12`; crypto_alt avg `-2.3967` n `230`; crypto_major avg `-3.1738` n `8`; equity avg `-4.8927` n `94`; fx avg `-0.0556` n `6`; index avg `-0.6353` n `25`; metal avg `-0.5397` n `20`; unknown avg `-0.3917` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
