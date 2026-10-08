# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T05:07:28.111524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.338` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0117` n `13`; crypto_alt avg `0.1057` n `235`; crypto_major avg `0.0309` n `8`; equity avg `0.0311` n `150`; fx avg `-0.0053` n `6`; index avg `0.0132` n `26`; metal avg `-0.0099` n `20`; unknown avg `-0.0824` n `1075`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.4396` n `235`; crypto_major avg `-0.4897` n `8`; equity avg `0.1511` n `150`; fx avg `0.0128` n `6`; index avg `0.0547` n `26`; metal avg `-0.0307` n `20`; unknown avg `-0.2174` n `1075`
- 4h: commodity avg `0.1667` n `13`; crypto_alt avg `-1.4054` n `235`; crypto_major avg `-1.341` n `8`; equity avg `-0.4634` n `150`; fx avg `0.0527` n `6`; index avg `-0.003` n `26`; metal avg `0.0447` n `20`; unknown avg `0.123` n `1069`
- 24h: commodity avg `0.4331` n `13`; crypto_alt avg `-0.9902` n `235`; crypto_major avg `-2.1975` n `8`; equity avg `-1.2826` n `150`; fx avg `-0.1151` n `6`; index avg `-0.2071` n `26`; metal avg `-0.1588` n `20`; unknown avg `247.1262` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
