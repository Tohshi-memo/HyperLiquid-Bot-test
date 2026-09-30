# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T10:52:27.236922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `12`; crypto_alt avg `-0.021` n `234`; crypto_major avg `0.0376` n `8`; equity avg `0.012` n `142`; fx avg `-0.0042` n `6`; index avg `0.0055` n `26`; metal avg `-0.0291` n `20`; unknown avg `4.2363` n `963`
- 1h: commodity avg `0.0908` n `12`; crypto_alt avg `0.1332` n `234`; crypto_major avg `0.39` n `8`; equity avg `-0.0252` n `142`; fx avg `0.0212` n `6`; index avg `-0.0113` n `26`; metal avg `0.0124` n `20`; unknown avg `5.369` n `961`
- 4h: commodity avg `0.1813` n `12`; crypto_alt avg `1.5255` n `234`; crypto_major avg `1.2876` n `8`; equity avg `0.0959` n `142`; fx avg `0.0751` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0595` n `20`; unknown avg `3.5183` n `943`
- 24h: commodity avg `-0.2172` n `12`; crypto_alt avg `0.3072` n `234`; crypto_major avg `-0.1368` n `8`; equity avg `0.0346` n `142`; fx avg `0.0422` n `6`; index avg `0.022` n `26`; metal avg `0.1487` n `20`; unknown avg `2928.4947` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
