# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T20:07:26.131785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.675` n `228`; crypto_major avg `-0.5595` n `8`; equity avg `-0.4118` n `74`; fx avg `0.0085` n `6`; index avg `-0.1241` n `23`; metal avg `-0.0105` n `18`; unknown avg `0.9222` n `424`
- 1h: commodity avg `-0.1271` n `12`; crypto_alt avg `-0.7423` n `228`; crypto_major avg `-0.6373` n `8`; equity avg `-0.6085` n `74`; fx avg `-0.0195` n `6`; index avg `-0.2132` n `23`; metal avg `-0.0676` n `18`; unknown avg `0.8417` n `424`
- 4h: commodity avg `0.1904` n `12`; crypto_alt avg `-0.9651` n `228`; crypto_major avg `-0.8292` n `8`; equity avg `-0.52` n `74`; fx avg `-0.0468` n `6`; index avg `0.1596` n `23`; metal avg `-0.0198` n `18`; unknown avg `1.6625` n `424`
- 24h: commodity avg `-0.7116` n `12`; crypto_alt avg `-5.4586` n `228`; crypto_major avg `-3.7748` n `8`; equity avg `-1.4056` n `73`; fx avg `0.013` n `6`; index avg `-0.0945` n `23`; metal avg `0.9459` n `18`; unknown avg `0.6181` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
