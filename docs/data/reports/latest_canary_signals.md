# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T12:22:36.621154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `12`; crypto_alt avg `0.0969` n `230`; crypto_major avg `0.0311` n `8`; equity avg `-0.2513` n `102`; fx avg `-0.0082` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0302` n `20`; unknown avg `-0.035` n `780`
- 1h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.2208` n `230`; crypto_major avg `-0.1148` n `8`; equity avg `-0.4805` n `102`; fx avg `-0.0067` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0458` n `20`; unknown avg `0.2252` n `780`
- 4h: commodity avg `0.6469` n `12`; crypto_alt avg `-0.5329` n `230`; crypto_major avg `-0.2685` n `8`; equity avg `-0.3396` n `102`; fx avg `0.1039` n `6`; index avg `-0.0578` n `25`; metal avg `-0.1506` n `20`; unknown avg `0.9249` n `780`
- 24h: commodity avg `0.519` n `12`; crypto_alt avg `-0.6202` n `230`; crypto_major avg `-0.386` n `8`; equity avg `6.0619` n `102`; fx avg `-0.0909` n `6`; index avg `0.8956` n `25`; metal avg `0.0212` n `20`; unknown avg `1.0478` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
