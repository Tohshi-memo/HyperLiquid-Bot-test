# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:03:40.545184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `-0.0547` n `231`; crypto_major avg `-0.0308` n `8`; equity avg `-0.0231` n `122`; fx avg `0.004` n `6`; index avg `-0.0368` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0311` n `797`
- 1h: commodity avg `0.247` n `12`; crypto_alt avg `-0.1019` n `231`; crypto_major avg `-0.0555` n `8`; equity avg `-0.145` n `122`; fx avg `0.0105` n `6`; index avg `-0.0317` n `25`; metal avg `-0.106` n `20`; unknown avg `0.0526` n `797`
- 4h: commodity avg `0.5785` n `12`; crypto_alt avg `-1.1985` n `231`; crypto_major avg `-0.978` n `8`; equity avg `-0.3086` n `122`; fx avg `-0.0112` n `6`; index avg `-0.0265` n `25`; metal avg `-0.2971` n `20`; unknown avg `-0.1694` n `797`
- 24h: commodity avg `0.4472` n `12`; crypto_alt avg `-2.4393` n `231`; crypto_major avg `-2.348` n `8`; equity avg `-0.6353` n `122`; fx avg `-0.0434` n `6`; index avg `-0.0206` n `25`; metal avg `-0.3159` n `20`; unknown avg `0.2854` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `670`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `670`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1015`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `670`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0701`, n `670`, weak_sample_signal
