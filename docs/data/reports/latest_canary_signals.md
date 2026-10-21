# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T07:52:34.294478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `13`; crypto_alt avg `0.2102` n `237`; crypto_major avg `0.2893` n `8`; equity avg `-0.0233` n `151`; fx avg `0.0166` n `6`; index avg `-0.007` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.1041` n `1200`
- 1h: commodity avg `-0.1496` n `13`; crypto_alt avg `0.7601` n `237`; crypto_major avg `0.6814` n `8`; equity avg `0.1378` n `151`; fx avg `0.0088` n `6`; index avg `0.0349` n `26`; metal avg `0.0845` n `20`; unknown avg `3.0389` n `1196`
- 4h: commodity avg `-0.1696` n `13`; crypto_alt avg `0.6653` n `237`; crypto_major avg `0.6396` n `8`; equity avg `-0.0615` n `151`; fx avg `-0.0048` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0651` n `20`; unknown avg `1.7124` n `1168`
- 24h: commodity avg `-0.2561` n `13`; crypto_alt avg `3.5456` n `237`; crypto_major avg `2.7098` n `8`; equity avg `2.7466` n `151`; fx avg `0.0143` n `6`; index avg `0.3653` n `26`; metal avg `-0.0882` n `20`; unknown avg `5293.0229` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
