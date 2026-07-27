# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T01:22:26.288088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `-0.1129` n `230`; crypto_major avg `-0.1452` n `8`; equity avg `-0.2546` n `100`; fx avg `-0.0052` n `6`; index avg `-0.0916` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.003` n `775`
- 1h: commodity avg `0.182` n `12`; crypto_alt avg `-0.1493` n `230`; crypto_major avg `-0.1578` n `8`; equity avg `-0.2916` n `100`; fx avg `0.0381` n `6`; index avg `-0.1288` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.247` n `775`
- 4h: commodity avg `-0.2444` n `12`; crypto_alt avg `0.6712` n `230`; crypto_major avg `0.5456` n `8`; equity avg `-0.037` n `100`; fx avg `0.0667` n `6`; index avg `-0.0583` n `25`; metal avg `0.2074` n `20`; unknown avg `-0.2397` n `775`
- 24h: commodity avg `-0.4507` n `12`; crypto_alt avg `1.457` n `230`; crypto_major avg `1.4292` n `8`; equity avg `0.4848` n `100`; fx avg `0.1201` n `6`; index avg `0.0132` n `25`; metal avg `0.4298` n `20`; unknown avg `0.018` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
