# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T13:37:25.849889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.329` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `0.5973` n `231`; crypto_major avg `0.6682` n `8`; equity avg `0.2363` n `122`; fx avg `0.0014` n `6`; index avg `0.018` n `25`; metal avg `0.0476` n `20`; unknown avg `0.203` n `795`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `0.0307` n `231`; crypto_major avg `0.13` n `8`; equity avg `0.3515` n `122`; fx avg `0.0443` n `6`; index avg `0.0189` n `25`; metal avg `-0.0759` n `20`; unknown avg `-0.0207` n `795`
- 4h: commodity avg `-0.0831` n `12`; crypto_alt avg `-1.1688` n `231`; crypto_major avg `-1.331` n `8`; equity avg `0.107` n `122`; fx avg `0.0118` n `6`; index avg `-0.002` n `25`; metal avg `-0.117` n `20`; unknown avg `-0.1162` n `794`
- 24h: commodity avg `-0.9887` n `12`; crypto_alt avg `-0.8047` n `231`; crypto_major avg `-0.3745` n `8`; equity avg `1.8637` n `122`; fx avg `0.0418` n `6`; index avg `0.2638` n `25`; metal avg `-0.5773` n `20`; unknown avg `-0.949` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
