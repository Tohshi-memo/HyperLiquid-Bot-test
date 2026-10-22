# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T18:07:32.998349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.32` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7985` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0744` n `13`; crypto_alt avg `-0.2933` n `237`; crypto_major avg `-0.2001` n `8`; equity avg `-0.2139` n `151`; fx avg `-0.0037` n `6`; index avg `-0.0242` n `26`; metal avg `-0.0332` n `20`; unknown avg `-0.7297` n `1231`
- 1h: commodity avg `0.1602` n `13`; crypto_alt avg `0.0149` n `237`; crypto_major avg `-0.0594` n `8`; equity avg `-0.1899` n `151`; fx avg `0.0084` n `6`; index avg `-0.0032` n `26`; metal avg `0.0203` n `20`; unknown avg `-0.1548` n `1231`
- 4h: commodity avg `0.1806` n `13`; crypto_alt avg `-1.3499` n `237`; crypto_major avg `-1.0682` n `8`; equity avg `-2.8667` n `151`; fx avg `0.0447` n `6`; index avg `-0.2637` n `26`; metal avg `-0.1707` n `20`; unknown avg `-0.0321` n `1117`
- 24h: commodity avg `0.6365` n `13`; crypto_alt avg `-5.2574` n `237`; crypto_major avg `-4.1945` n `8`; equity avg `-5.4236` n `151`; fx avg `-0.1297` n `6`; index avg `-0.665` n `26`; metal avg `-0.9712` n `20`; unknown avg `3.0385` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
