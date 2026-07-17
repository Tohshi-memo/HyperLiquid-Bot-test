# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T22:07:33.051224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0285` n `230`; crypto_major avg `-0.0264` n `8`; equity avg `-0.0289` n `96`; fx avg `0.0005` n `6`; index avg `-0.0091` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.0445` n `769`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.1669` n `230`; crypto_major avg `-0.119` n `8`; equity avg `-0.0549` n `96`; fx avg `-0.0191` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.05` n `769`
- 4h: commodity avg `0.0275` n `12`; crypto_alt avg `-0.4338` n `230`; crypto_major avg `-0.0909` n `8`; equity avg `-0.9845` n `96`; fx avg `-0.0498` n `6`; index avg `-0.1197` n `25`; metal avg `-0.0223` n `20`; unknown avg `-0.238` n `769`
- 24h: commodity avg `0.6907` n `12`; crypto_alt avg `-1.5952` n `230`; crypto_major avg `-1.3902` n `8`; equity avg `-1.6118` n `94`; fx avg `0.0533` n `6`; index avg `-0.341` n `25`; metal avg `-0.0273` n `20`; unknown avg `-0.0616` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
