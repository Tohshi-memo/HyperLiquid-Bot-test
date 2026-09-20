# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T12:16:26.771454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.0481` n `234`; crypto_major avg `-0.0348` n `8`; equity avg `0.0222` n `140`; fx avg `-0.0214` n `6`; index avg `-0.0009` n `26`; metal avg `0.0103` n `20`; unknown avg `0.0822` n `943`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `0.53` n `234`; crypto_major avg `0.4365` n `8`; equity avg `0.0667` n `140`; fx avg `-0.021` n `6`; index avg `0.0116` n `26`; metal avg `0.0036` n `20`; unknown avg `0.2234` n `935`
- 4h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.0644` n `234`; crypto_major avg `0.2199` n `8`; equity avg `0.0052` n `140`; fx avg `-0.0072` n `6`; index avg `0.0126` n `26`; metal avg `-0.0151` n `20`; unknown avg `0.3988` n `935`
- 24h: commodity avg `0.2715` n `12`; crypto_alt avg `-2.0771` n `234`; crypto_major avg `-2.0383` n `8`; equity avg `-0.233` n `140`; fx avg `-0.0529` n `6`; index avg `-0.0496` n `26`; metal avg `-0.0182` n `20`; unknown avg `0.3139` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
