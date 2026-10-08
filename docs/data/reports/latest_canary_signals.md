# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T03:22:27.097707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `-0.0242` n `235`; crypto_major avg `-0.0639` n `8`; equity avg `-0.1243` n `150`; fx avg `-0.0015` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.1068` n `1077`
- 1h: commodity avg `0.039` n `13`; crypto_alt avg `-0.316` n `235`; crypto_major avg `-0.3257` n `8`; equity avg `-0.3711` n `150`; fx avg `0.0224` n `6`; index avg `-0.0586` n `26`; metal avg `-0.0559` n `20`; unknown avg `-0.076` n `1075`
- 4h: commodity avg `0.229` n `13`; crypto_alt avg `-0.0987` n `235`; crypto_major avg `-0.2446` n `8`; equity avg `-0.4853` n `150`; fx avg `-0.0075` n `6`; index avg `-0.0913` n `26`; metal avg `0.3023` n `20`; unknown avg `-0.3229` n `1069`
- 24h: commodity avg `0.4631` n `13`; crypto_alt avg `-0.7224` n `235`; crypto_major avg `-1.523` n `8`; equity avg `-1.2103` n `150`; fx avg `-0.1297` n `6`; index avg `-0.2275` n `26`; metal avg `-0.1545` n `20`; unknown avg `246.9538` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1534`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1333`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.118`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0953`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `669`, weak_sample_signal
