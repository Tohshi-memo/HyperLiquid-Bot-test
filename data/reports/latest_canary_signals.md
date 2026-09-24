# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T23:07:33.520326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.2974` n `234`; crypto_major avg `0.1588` n `8`; equity avg `0.0133` n `141`; fx avg `0.0283` n `6`; index avg `-0.0045` n `26`; metal avg `0.0175` n `20`; unknown avg `2.4073` n `944`
- 1h: commodity avg `-0.0726` n `12`; crypto_alt avg `0.1586` n `234`; crypto_major avg `0.0592` n `8`; equity avg `0.0115` n `141`; fx avg `0.0132` n `6`; index avg `-0.0128` n `26`; metal avg `0.0157` n `20`; unknown avg `4.9188` n `904`
- 4h: commodity avg `-0.3651` n `12`; crypto_alt avg `0.1807` n `234`; crypto_major avg `-0.3494` n `8`; equity avg `-0.0523` n `141`; fx avg `-0.0186` n `6`; index avg `-0.0334` n `26`; metal avg `-0.0076` n `20`; unknown avg `9.3194` n `829`
- 24h: commodity avg `0.6349` n `12`; crypto_alt avg `3.8843` n `234`; crypto_major avg `0.852` n `8`; equity avg `-0.3343` n `141`; fx avg `0.0425` n `6`; index avg `-0.1348` n `26`; metal avg `-0.1175` n `20`; unknown avg `22.8253` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
