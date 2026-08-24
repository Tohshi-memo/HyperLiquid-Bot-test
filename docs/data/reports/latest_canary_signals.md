# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T03:22:29.159799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5709` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3093` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.1454` n `231`; crypto_major avg `-0.1979` n `8`; equity avg `-0.0824` n `122`; fx avg `-0.0098` n `6`; index avg `-0.0297` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0047` n `793`
- 1h: commodity avg `0.0767` n `12`; crypto_alt avg `-0.3904` n `231`; crypto_major avg `-0.5821` n `8`; equity avg `-0.506` n `122`; fx avg `0.0196` n `6`; index avg `-0.0796` n `25`; metal avg `-0.0721` n `20`; unknown avg `0.0048` n `793`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `-1.9635` n `231`; crypto_major avg `-1.4891` n `8`; equity avg `-1.699` n `122`; fx avg `-0.0655` n `6`; index avg `-0.1798` n `25`; metal avg `0.0818` n `20`; unknown avg `0.5738` n `793`
- 24h: commodity avg `-0.2835` n `12`; crypto_alt avg `2.7356` n `231`; crypto_major avg `0.3056` n `8`; equity avg `-1.026` n `122`; fx avg `-0.2031` n `6`; index avg `-0.0841` n `25`; metal avg `0.1222` n `20`; unknown avg `5.9365` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
