# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T04:22:26.864623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6451` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6041` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0198` n `13`; crypto_alt avg `0.3074` n `238`; crypto_major avg `0.2851` n `8`; equity avg `0.2927` n `155`; fx avg `0.0083` n `6`; index avg `0.0661` n `27`; metal avg `0.0128` n `20`; unknown avg `0.1665` n `1236`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.2726` n `238`; crypto_major avg `0.26` n `8`; equity avg `0.4268` n `155`; fx avg `0.0073` n `6`; index avg `0.1145` n `27`; metal avg `0.0179` n `20`; unknown avg `0.1247` n `1220`
- 4h: commodity avg `-0.0721` n `13`; crypto_alt avg `-2.6863` n `238`; crypto_major avg `-1.7889` n `8`; equity avg `-1.0722` n `155`; fx avg `-0.0363` n `6`; index avg `-0.1438` n `27`; metal avg `-0.1848` n `20`; unknown avg `2.6087` n `1208`
- 24h: commodity avg `-0.0581` n `13`; crypto_alt avg `-2.3174` n `238`; crypto_major avg `-1.6159` n `8`; equity avg `-1.1695` n `154`; fx avg `0.0026` n `6`; index avg `-0.082` n `27`; metal avg `-0.24` n `20`; unknown avg `27.5009` n `978`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
