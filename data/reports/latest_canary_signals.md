# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T16:07:27.442829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.9172` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6249` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.56` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0652` n `13`; crypto_alt avg `0.1579` n `239`; crypto_major avg `0.1276` n `8`; equity avg `0.2277` n `168`; fx avg `0.0078` n `6`; index avg `0.0349` n `27`; metal avg `-0.0539` n `20`; unknown avg `0.8807` n `1244`
- 1h: commodity avg `-0.0769` n `13`; crypto_alt avg `0.9623` n `239`; crypto_major avg `1.4623` n `8`; equity avg `1.484` n `168`; fx avg `-0.0165` n `6`; index avg `0.1504` n `27`; metal avg `-0.0977` n `20`; unknown avg `2.0732` n `1252`
- 4h: commodity avg `-0.3708` n `13`; crypto_alt avg `-1.6348` n `239`; crypto_major avg `-1.8867` n `8`; equity avg `-0.2618` n `168`; fx avg `-0.0562` n `6`; index avg `0.0305` n `27`; metal avg `-0.4659` n `20`; unknown avg `2.1428` n `1249`
- 24h: commodity avg `-0.4842` n `13`; crypto_alt avg `0.4236` n `239`; crypto_major avg `0.9311` n `8`; equity avg `2.6725` n `168`; fx avg `-0.137` n `6`; index avg `0.258` n `27`; metal avg `0.5889` n `20`; unknown avg `279.4159` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
