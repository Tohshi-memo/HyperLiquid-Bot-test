# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T16:07:45.010240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.426` n `234`; crypto_major avg `0.1859` n `8`; equity avg `0.0323` n `142`; fx avg `-0.0123` n `6`; index avg `0.0136` n `26`; metal avg `0.0011` n `20`; unknown avg `1.9627` n `961`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.8251` n `234`; crypto_major avg `0.8326` n `8`; equity avg `0.0348` n `142`; fx avg `-0.021` n `6`; index avg `0.0148` n `26`; metal avg `-0.0006` n `20`; unknown avg `2.6048` n `953`
- 4h: commodity avg `0.1818` n `12`; crypto_alt avg `0.5232` n `234`; crypto_major avg `0.3192` n `8`; equity avg `0.1945` n `142`; fx avg `-0.0146` n `6`; index avg `0.1507` n `26`; metal avg `-0.1931` n `20`; unknown avg `7.3831` n `875`
- 24h: commodity avg `0.1362` n `12`; crypto_alt avg `1.3076` n `234`; crypto_major avg `1.1077` n `8`; equity avg `-0.1207` n `142`; fx avg `0.0665` n `6`; index avg `0.1765` n `26`; metal avg `0.0261` n `20`; unknown avg `16.2288` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
