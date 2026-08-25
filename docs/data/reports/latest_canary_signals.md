# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:22:26.607605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0865` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7718` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5388` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.0505` n `231`; crypto_major avg `-0.0538` n `8`; equity avg `-0.0623` n `122`; fx avg `-0.0015` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0226` n `795`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.5495` n `231`; crypto_major avg `-0.7387` n `8`; equity avg `0.1627` n `122`; fx avg `-0.0161` n `6`; index avg `0.029` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.1376` n `794`
- 4h: commodity avg `-0.3308` n `12`; crypto_alt avg `-1.576` n `231`; crypto_major avg `-1.6721` n `8`; equity avg `0.4144` n `122`; fx avg `0.0122` n `6`; index avg `0.0997` n `25`; metal avg `-0.1333` n `20`; unknown avg `-0.2516` n `794`
- 24h: commodity avg `-0.6186` n `12`; crypto_alt avg `0.0869` n `231`; crypto_major avg `0.9653` n `8`; equity avg `0.672` n `122`; fx avg `0.0385` n `6`; index avg `0.1282` n `25`; metal avg `-0.2366` n `20`; unknown avg `0.0557` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
