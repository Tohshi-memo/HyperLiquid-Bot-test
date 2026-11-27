# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T18:22:26.181728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4162` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.1064` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0712` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0523` n `13`; crypto_alt avg `0.5109` n `239`; crypto_major avg `0.5792` n `8`; equity avg `0.9302` n `168`; fx avg `-0.0017` n `6`; index avg `0.0808` n `27`; metal avg `0.1611` n `20`; unknown avg `22.1633` n `1250`
- 1h: commodity avg `-0.0195` n `13`; crypto_alt avg `0.2839` n `239`; crypto_major avg `0.0249` n `8`; equity avg `0.8807` n `168`; fx avg `-0.0031` n `6`; index avg `0.0807` n `27`; metal avg `0.1303` n `20`; unknown avg `160.3306` n `1258`
- 4h: commodity avg `-0.2251` n `13`; crypto_alt avg `-1.4394` n `239`; crypto_major avg `-2.0263` n `8`; equity avg `0.3899` n `168`; fx avg `-0.0656` n `6`; index avg `0.0801` n `27`; metal avg `0.0449` n `20`; unknown avg `164.2607` n `1242`
- 24h: commodity avg `-0.4919` n `13`; crypto_alt avg `0.3988` n `239`; crypto_major avg `0.7218` n `8`; equity avg `3.864` n `168`; fx avg `-0.1532` n `6`; index avg `0.3567` n `27`; metal avg `0.8851` n `20`; unknown avg `183.2483` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
