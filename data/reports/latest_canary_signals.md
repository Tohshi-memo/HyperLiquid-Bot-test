# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T14:52:32.303079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.189` n `229`; crypto_major avg `0.2243` n `8`; equity avg `0.0916` n `91`; fx avg `0.0072` n `6`; index avg `0.0229` n `25`; metal avg `0.0789` n `20`; unknown avg `-0.0189` n `766`
- 1h: commodity avg `0.0668` n `12`; crypto_alt avg `-0.8332` n `229`; crypto_major avg `-0.9874` n `8`; equity avg `-0.5319` n `91`; fx avg `0.0055` n `6`; index avg `-0.0231` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.0932` n `766`
- 4h: commodity avg `-0.3147` n `12`; crypto_alt avg `-0.7808` n `229`; crypto_major avg `-0.9175` n `8`; equity avg `-0.7254` n `91`; fx avg `-0.0474` n `6`; index avg `-0.0018` n `25`; metal avg `0.0728` n `20`; unknown avg `-0.1883` n `766`
- 24h: commodity avg `-0.6314` n `12`; crypto_alt avg `0.5394` n `229`; crypto_major avg `1.0373` n `8`; equity avg `-0.7055` n `91`; fx avg `-0.1246` n `6`; index avg `0.069` n `25`; metal avg `-0.081` n `20`; unknown avg `-0.1674` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
