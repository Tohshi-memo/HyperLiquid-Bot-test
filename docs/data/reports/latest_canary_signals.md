# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T01:22:27.060970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0416` n `230`; crypto_major avg `0.1166` n `8`; equity avg `0.243` n `107`; fx avg `0.029` n `6`; index avg `0.0388` n `25`; metal avg `0.0468` n `20`; unknown avg `-0.1087` n `780`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.1179` n `230`; crypto_major avg `-0.0279` n `8`; equity avg `-0.3731` n `107`; fx avg `-0.0637` n `6`; index avg `-0.1301` n `25`; metal avg `-0.042` n `20`; unknown avg `-0.1237` n `780`
- 4h: commodity avg `0.1085` n `12`; crypto_alt avg `-0.5044` n `230`; crypto_major avg `-0.4581` n `8`; equity avg `-0.4263` n `107`; fx avg `-0.0175` n `6`; index avg `-0.0976` n `25`; metal avg `-0.0197` n `20`; unknown avg `-0.0277` n `780`
- 24h: commodity avg `0.0566` n `12`; crypto_alt avg `0.541` n `230`; crypto_major avg `0.414` n `8`; equity avg `1.2997` n `107`; fx avg `-0.0324` n `6`; index avg `0.0867` n `25`; metal avg `-0.1245` n `20`; unknown avg `0.1208` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
