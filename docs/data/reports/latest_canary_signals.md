# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T15:22:26.527753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6689` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `2.1795` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0208` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0808` n `13`; crypto_alt avg `-0.7686` n `239`; crypto_major avg `-0.8302` n `8`; equity avg `-1.0916` n `162`; fx avg `-0.006` n `6`; index avg `-0.083` n `27`; metal avg `-0.1071` n `20`; unknown avg `0.0825` n `1262`
- 1h: commodity avg `-0.0721` n `13`; crypto_alt avg `-1.2827` n `239`; crypto_major avg `-1.3133` n `8`; equity avg `-3.4928` n `162`; fx avg `0.0074` n `6`; index avg `-0.2925` n `27`; metal avg `-0.0332` n `20`; unknown avg `27.6525` n `1256`
- 4h: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.2607` n `239`; crypto_major avg `-0.7884` n `8`; equity avg `-3.4573` n `162`; fx avg `0.0106` n `6`; index avg `-0.3108` n `27`; metal avg `-0.1262` n `20`; unknown avg `71.469` n `1250`
- 24h: commodity avg `0.4013` n `13`; crypto_alt avg `0.8823` n `239`; crypto_major avg `-1.0545` n `8`; equity avg `-2.9707` n `162`; fx avg `0.0067` n `6`; index avg `-0.2402` n `27`; metal avg `0.0477` n `20`; unknown avg `7.4642` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
