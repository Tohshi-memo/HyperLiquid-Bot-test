# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T13:37:28.738129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0757` n `12`; crypto_alt avg `0.1565` n `229`; crypto_major avg `0.1843` n `8`; equity avg `-0.1909` n `91`; fx avg `-0.0056` n `6`; index avg `0.0138` n `25`; metal avg `-0.0145` n `20`; unknown avg `0.0016` n `766`
- 1h: commodity avg `-0.1674` n `12`; crypto_alt avg `0.0469` n `229`; crypto_major avg `-0.0489` n `8`; equity avg `-0.3568` n `91`; fx avg `-0.0394` n `6`; index avg `-0.0197` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.0747` n `766`
- 4h: commodity avg `-0.0908` n `12`; crypto_alt avg `0.068` n `229`; crypto_major avg `-0.205` n `8`; equity avg `0.0032` n `91`; fx avg `-0.0315` n `6`; index avg `0.0088` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0708` n `766`
- 24h: commodity avg `-0.7855` n `12`; crypto_alt avg `1.271` n `229`; crypto_major avg `1.7352` n `8`; equity avg `-0.3272` n `91`; fx avg `-0.1199` n `6`; index avg `-0.0278` n `25`; metal avg `-0.1286` n `20`; unknown avg `-0.0775` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
