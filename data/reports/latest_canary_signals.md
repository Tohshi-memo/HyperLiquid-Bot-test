# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T13:26:04.355904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.9867` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9224` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.8442` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.07` n `12`; crypto_alt avg `-0.8777` n `231`; crypto_major avg `-0.8211` n `8`; equity avg `0.0512` n `122`; fx avg `0.0226` n `6`; index avg `0.004` n `25`; metal avg `-0.0693` n `20`; unknown avg `-0.2088` n `795`
- 1h: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.4311` n `231`; crypto_major avg `-0.3716` n `8`; equity avg `-0.04` n `122`; fx avg `0.0486` n `6`; index avg `-0.0404` n `25`; metal avg `-0.1704` n `20`; unknown avg `-0.1283` n `795`
- 4h: commodity avg `-0.1145` n `12`; crypto_alt avg `-1.7366` n `231`; crypto_major avg `-1.9908` n `8`; equity avg `-0.0684` n `122`; fx avg `0.0037` n `6`; index avg `-0.0041` n `25`; metal avg `-0.1466` n `20`; unknown avg `-0.2657` n `794`
- 24h: commodity avg `-0.9528` n `12`; crypto_alt avg `-2.2595` n `231`; crypto_major avg `-1.7713` n `8`; equity avg `0.6464` n `122`; fx avg `0.0415` n `6`; index avg `0.1313` n `25`; metal avg `-0.5658` n `20`; unknown avg `-0.7531` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
