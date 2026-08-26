# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T14:22:30.892264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0799` n `12`; crypto_alt avg `-0.0062` n `231`; crypto_major avg `-0.1371` n `8`; equity avg `-0.4758` n `122`; fx avg `-0.0052` n `6`; index avg `-0.0633` n `25`; metal avg `0.0177` n `20`; unknown avg `-0.0107` n `797`
- 1h: commodity avg `0.2339` n `12`; crypto_alt avg `0.2178` n `231`; crypto_major avg `0.3905` n `8`; equity avg `0.1941` n `122`; fx avg `-0.0078` n `6`; index avg `0.019` n `25`; metal avg `0.048` n `20`; unknown avg `0.0922` n `797`
- 4h: commodity avg `0.3692` n `12`; crypto_alt avg `-0.1146` n `231`; crypto_major avg `-0.2531` n `8`; equity avg `-0.319` n `122`; fx avg `-0.0045` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0513` n `20`; unknown avg `-0.1469` n `797`
- 24h: commodity avg `0.1405` n `12`; crypto_alt avg `-1.0122` n `231`; crypto_major avg `-1.0369` n `8`; equity avg `0.1405` n `122`; fx avg `-0.0665` n `6`; index avg `0.0365` n `25`; metal avg `0.1209` n `20`; unknown avg `0.5853` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
