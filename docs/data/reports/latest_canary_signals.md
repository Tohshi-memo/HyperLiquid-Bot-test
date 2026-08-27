# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T01:07:23.770684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `-0.1302` n `231`; crypto_major avg `-0.0858` n `8`; equity avg `0.2511` n `124`; fx avg `0.0049` n `6`; index avg `0.0107` n `25`; metal avg `0.1306` n `20`; unknown avg `1.0964` n `795`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.6338` n `231`; crypto_major avg `-0.6079` n `8`; equity avg `-0.6962` n `124`; fx avg `-0.0673` n `6`; index avg `-0.1483` n `25`; metal avg `0.0487` n `20`; unknown avg `-0.0638` n `795`
- 4h: commodity avg `0.0553` n `12`; crypto_alt avg `1.2497` n `231`; crypto_major avg `0.9994` n `8`; equity avg `0.0711` n `124`; fx avg `-0.0778` n `6`; index avg `-0.0123` n `25`; metal avg `0.2186` n `20`; unknown avg `0.4804` n `795`
- 24h: commodity avg `0.4716` n `12`; crypto_alt avg `0.6423` n `231`; crypto_major avg `0.4837` n `8`; equity avg `1.4679` n `124`; fx avg `-0.1504` n `6`; index avg `0.2665` n `25`; metal avg `-0.1337` n `20`; unknown avg `0.9359` n `778`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
