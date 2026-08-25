# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T13:52:28.671435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8343` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8089` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.6736` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6258` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.426` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-1.1023` n `231`; crypto_major avg `-1.1692` n `8`; equity avg `0.0114` n `122`; fx avg `-0.0045` n `6`; index avg `-0.0049` n `25`; metal avg `-0.035` n `20`; unknown avg `-0.3042` n `795`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `-1.4456` n `231`; crypto_major avg `-1.4155` n `8`; equity avg `0.2581` n `122`; fx avg `0.0302` n `6`; index avg `0.0105` n `25`; metal avg `-0.1862` n `20`; unknown avg `-0.3866` n `795`
- 4h: commodity avg `-0.069` n `12`; crypto_alt avg `-1.7366` n `231`; crypto_major avg `-1.8495` n `8`; equity avg `-0.0152` n `122`; fx avg `0.0133` n `6`; index avg `-0.0406` n `25`; metal avg `-0.2237` n `20`; unknown avg `-0.2884` n `794`
- 24h: commodity avg `-0.8933` n `12`; crypto_alt avg `-1.2326` n `231`; crypto_major avg `-0.7973` n `8`; equity avg `2.6362` n `122`; fx avg `0.0406` n `6`; index avg `0.3806` n `25`; metal avg `-0.5047` n `20`; unknown avg `-0.9623` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
