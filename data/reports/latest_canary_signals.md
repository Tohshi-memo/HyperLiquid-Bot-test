# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T09:37:27.141108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5544` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2291` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `0.0129` n `231`; crypto_major avg `-0.0075` n `8`; equity avg `0.0555` n `122`; fx avg `-0.0066` n `6`; index avg `0.0158` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.0508` n `794`
- 1h: commodity avg `-0.3004` n `12`; crypto_alt avg `-0.1208` n `231`; crypto_major avg `-0.1799` n `8`; equity avg `0.3049` n `122`; fx avg `0.0038` n `6`; index avg `0.0795` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0743` n `794`
- 4h: commodity avg `-0.5443` n `12`; crypto_alt avg `-1.2312` n `231`; crypto_major avg `-1.101` n `8`; equity avg `0.4534` n `122`; fx avg `0.0388` n `6`; index avg `0.1281` n `25`; metal avg `-0.1086` n `20`; unknown avg `-0.2985` n `778`
- 24h: commodity avg `-0.6868` n `12`; crypto_alt avg `0.8175` n `231`; crypto_major avg `1.9681` n `8`; equity avg `0.5179` n `122`; fx avg `0.0767` n `6`; index avg `0.1092` n `25`; metal avg `-0.1708` n `20`; unknown avg `-0.0115` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
