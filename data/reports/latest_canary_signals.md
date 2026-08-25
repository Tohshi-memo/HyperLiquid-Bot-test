# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:07:30.933606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1194` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6928` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1002` n `12`; crypto_alt avg `0.0159` n `231`; crypto_major avg `-0.0317` n `8`; equity avg `0.0356` n `122`; fx avg `-0.002` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0594` n `20`; unknown avg `0.0419` n `794`
- 1h: commodity avg `-0.0504` n `12`; crypto_alt avg `-0.2692` n `231`; crypto_major avg `-0.4649` n `8`; equity avg `0.303` n `122`; fx avg `-0.009` n `6`; index avg `0.0477` n `25`; metal avg `0.0925` n `20`; unknown avg `-0.0086` n `794`
- 4h: commodity avg `-0.2818` n `12`; crypto_alt avg `-1.5026` n `231`; crypto_major avg `-1.5515` n `8`; equity avg `0.5679` n `122`; fx avg `0.0418` n `6`; index avg `0.1413` n `25`; metal avg `-0.0853` n `20`; unknown avg `-0.2481` n `794`
- 24h: commodity avg `-0.5989` n `12`; crypto_alt avg `0.1767` n `231`; crypto_major avg `1.1339` n `8`; equity avg `0.6079` n `122`; fx avg `0.0364` n `6`; index avg `0.1277` n `25`; metal avg `-0.2351` n `20`; unknown avg `-0.1347` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
