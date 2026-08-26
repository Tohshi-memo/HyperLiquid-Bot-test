# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T03:37:23.580162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.1764` n `231`; crypto_major avg `-0.0778` n `8`; equity avg `0.0033` n `122`; fx avg `-0.0216` n `6`; index avg `-0.0024` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0836` n `797`
- 1h: commodity avg `-0.0745` n `12`; crypto_alt avg `-0.3775` n `231`; crypto_major avg `-0.201` n `8`; equity avg `0.1442` n `122`; fx avg `-0.0008` n `6`; index avg `0.0361` n `25`; metal avg `-0.0345` n `20`; unknown avg `0.0948` n `797`
- 4h: commodity avg `-0.1477` n `12`; crypto_alt avg `0.9046` n `231`; crypto_major avg `0.5609` n `8`; equity avg `0.0448` n `122`; fx avg `0.0032` n `6`; index avg `0.0375` n `25`; metal avg `0.1066` n `20`; unknown avg `0.7607` n `796`
- 24h: commodity avg `-0.9171` n `12`; crypto_alt avg `-2.9139` n `231`; crypto_major avg `-2.9393` n `8`; equity avg `1.3958` n `122`; fx avg `0.0245` n `6`; index avg `0.2039` n `25`; metal avg `0.2753` n `20`; unknown avg `0.0482` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
