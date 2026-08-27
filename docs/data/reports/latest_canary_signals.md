# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T12:37:25.916893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.2506` n `231`; crypto_major avg `-0.3211` n `8`; equity avg `-0.04` n `127`; fx avg `0.0107` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0596` n `20`; unknown avg `-0.0284` n `792`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.0473` n `231`; crypto_major avg `-0.1033` n `8`; equity avg `-0.0137` n `127`; fx avg `0.0181` n `6`; index avg `0.0066` n `26`; metal avg `-0.0854` n `20`; unknown avg `-0.0012` n `792`
- 4h: commodity avg `0.229` n `12`; crypto_alt avg `-0.8321` n `231`; crypto_major avg `-0.6098` n `8`; equity avg `-0.2812` n `127`; fx avg `0.0029` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0892` n `20`; unknown avg `0.0185` n `792`
- 24h: commodity avg `0.5369` n `12`; crypto_alt avg `1.0409` n `231`; crypto_major avg `1.8118` n `8`; equity avg `2.1301` n `127`; fx avg `-0.0742` n `6`; index avg `0.3206` n `26`; metal avg `-0.3934` n `20`; unknown avg `0.5416` n `775`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
