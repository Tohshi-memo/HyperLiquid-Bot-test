# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T12:22:31.832731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0841` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8694` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7475` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `-0.0641` n `231`; crypto_major avg `-0.1657` n `8`; equity avg `0.0023` n `122`; fx avg `0.0023` n `6`; index avg `0.0089` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0164` n `795`
- 1h: commodity avg `-0.1391` n `12`; crypto_alt avg `-0.683` n `231`; crypto_major avg `-0.7143` n `8`; equity avg `0.0116` n `122`; fx avg `-0.0149` n `6`; index avg `0.0335` n `25`; metal avg `-0.0256` n `20`; unknown avg `-0.1383` n `795`
- 4h: commodity avg `-0.4454` n `12`; crypto_alt avg `-1.3479` n `231`; crypto_major avg `-1.7454` n `8`; equity avg `0.3387` n `122`; fx avg `-0.0537` n `6`; index avg `0.124` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0473` n `794`
- 24h: commodity avg `-0.8844` n `12`; crypto_alt avg `-0.9962` n `231`; crypto_major avg `-0.5699` n `8`; equity avg `0.5675` n `122`; fx avg `0.0155` n `6`; index avg `0.1429` n `25`; metal avg `-0.2945` n `20`; unknown avg `-0.3449` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
