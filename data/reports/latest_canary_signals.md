# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T16:07:27.530376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `0.036` n `230`; crypto_major avg `0.0268` n `8`; equity avg `-0.0098` n `114`; fx avg `0.0049` n `6`; index avg `0.0032` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0042` n `791`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `0.1385` n `230`; crypto_major avg `0.1138` n `8`; equity avg `0.0378` n `114`; fx avg `0.0141` n `6`; index avg `0.0009` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.0187` n `791`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `0.2463` n `230`; crypto_major avg `0.2289` n `8`; equity avg `0.0084` n `114`; fx avg `0.005` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0122` n `791`
- 24h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.1234` n `230`; crypto_major avg `0.1137` n `8`; equity avg `0.2992` n `114`; fx avg `-0.0015` n `6`; index avg `0.0262` n `25`; metal avg `0.0354` n `20`; unknown avg `0.1458` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
