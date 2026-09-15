# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T21:22:27.155239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7347` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6938` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0752` n `234`; crypto_major avg `-0.0991` n `8`; equity avg `-0.0664` n `137`; fx avg `0.0076` n `6`; index avg `-0.007` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.6178` n `919`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.0386` n `234`; crypto_major avg `-0.0493` n `8`; equity avg `-0.0457` n `137`; fx avg `-0.0209` n `6`; index avg `-0.0037` n `27`; metal avg `0.006` n `20`; unknown avg `9.1911` n `895`
- 4h: commodity avg `-0.0591` n `12`; crypto_alt avg `-1.4681` n `234`; crypto_major avg `-1.6521` n `8`; equity avg `-0.2504` n `137`; fx avg `-0.0038` n `6`; index avg `0.0417` n `27`; metal avg `0.0826` n `20`; unknown avg `1.206` n `876`
- 24h: commodity avg `0.4909` n `12`; crypto_alt avg `-4.3444` n `234`; crypto_major avg `-5.0843` n `8`; equity avg `-1.2779` n `137`; fx avg `0.203` n `6`; index avg `-0.0664` n `27`; metal avg `0.1325` n `20`; unknown avg `1.4242` n `826`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
