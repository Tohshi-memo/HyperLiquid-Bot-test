# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T21:07:27.626840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0806` n `13`; crypto_alt avg `0.1002` n `235`; crypto_major avg `0.1421` n `8`; equity avg `0.0268` n `150`; fx avg `-0.0045` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.0177` n `1106`
- 1h: commodity avg `0.0748` n `13`; crypto_alt avg `0.6458` n `235`; crypto_major avg `0.3961` n `8`; equity avg `0.0573` n `150`; fx avg `0.0003` n `6`; index avg `0.0146` n `26`; metal avg `0.0181` n `20`; unknown avg `3.1068` n `1060`
- 4h: commodity avg `-0.0358` n `13`; crypto_alt avg `-0.0499` n `235`; crypto_major avg `-0.1316` n `8`; equity avg `0.1816` n `150`; fx avg `0.0142` n `6`; index avg `0.0289` n `26`; metal avg `0.0448` n `20`; unknown avg `2.9902` n `1034`
- 24h: commodity avg `-0.1226` n `13`; crypto_alt avg `1.7344` n `235`; crypto_major avg `0.4798` n `8`; equity avg `0.8945` n `150`; fx avg `0.0088` n `6`; index avg `0.1446` n `26`; metal avg `0.6154` n `20`; unknown avg `13.3618` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
