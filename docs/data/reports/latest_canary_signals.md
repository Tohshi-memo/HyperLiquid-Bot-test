# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T03:07:30.917424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `13`; crypto_alt avg `-0.192` n `239`; crypto_major avg `-0.104` n `8`; equity avg `0.0874` n `161`; fx avg `-0.016` n `6`; index avg `0.0122` n `27`; metal avg `0.0398` n `20`; unknown avg `18.7716` n `1258`
- 1h: commodity avg `-0.0223` n `13`; crypto_alt avg `-0.0651` n `239`; crypto_major avg `0.0806` n `8`; equity avg `-0.0157` n `161`; fx avg `-0.0763` n `6`; index avg `0.0253` n `27`; metal avg `-0.0135` n `20`; unknown avg `18.7957` n `1256`
- 4h: commodity avg `-0.0337` n `13`; crypto_alt avg `0.0525` n `239`; crypto_major avg `0.1909` n `8`; equity avg `0.4964` n `161`; fx avg `-0.1142` n `6`; index avg `0.0446` n `27`; metal avg `0.0434` n `20`; unknown avg `22.7498` n `1250`
- 24h: commodity avg `0.1281` n `13`; crypto_alt avg `-1.703` n `239`; crypto_major avg `-0.483` n `8`; equity avg `1.4037` n `161`; fx avg `-0.1841` n `6`; index avg `0.1552` n `27`; metal avg `-0.3688` n `20`; unknown avg `2.6329` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
