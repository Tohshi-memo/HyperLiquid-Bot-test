# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T20:51:49.125023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4701` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1362` n `12`; crypto_alt avg `0.3893` n `228`; crypto_major avg `0.1787` n `8`; equity avg `-0.0408` n `67`; fx avg `-0.0105` n `6`; index avg `-0.0122` n `23`; metal avg `-0.0578` n `18`; unknown avg `0.1436` n `386`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `0.2059` n `228`; crypto_major avg `-0.0754` n `8`; equity avg `-0.0419` n `67`; fx avg `-0.0216` n `6`; index avg `-0.0251` n `23`; metal avg `-0.1156` n `18`; unknown avg `-0.1012` n `386`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `-2.4896` n `228`; crypto_major avg `-1.7005` n `8`; equity avg `-0.9228` n `67`; fx avg `0.0207` n `6`; index avg `-0.2304` n `23`; metal avg `-0.2006` n `18`; unknown avg `1.2911` n `386`
- 24h: commodity avg `-1.0518` n `12`; crypto_alt avg `-2.8319` n `228`; crypto_major avg `-2.009` n `8`; equity avg `-1.1361` n `67`; fx avg `0.1581` n `6`; index avg `0.4785` n `23`; metal avg `-1.054` n `18`; unknown avg `-1.2916` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
