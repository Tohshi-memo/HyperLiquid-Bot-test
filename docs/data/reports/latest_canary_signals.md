# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T11:52:29.115559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.063` n `238`; crypto_major avg `0.025` n `8`; equity avg `0.0583` n `156`; fx avg `-0.0089` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0009` n `20`; unknown avg `-0.022` n `1263`
- 1h: commodity avg `-0.0123` n `13`; crypto_alt avg `-0.159` n `238`; crypto_major avg `-0.0944` n `8`; equity avg `0.0371` n `156`; fx avg `-0.0109` n `6`; index avg `-0.0041` n `27`; metal avg `0.0125` n `20`; unknown avg `18.772` n `1257`
- 4h: commodity avg `-0.0389` n `13`; crypto_alt avg `-0.1663` n `238`; crypto_major avg `0.1642` n `8`; equity avg `0.2038` n `156`; fx avg `-0.0229` n `6`; index avg `0.0099` n `27`; metal avg `0.0299` n `20`; unknown avg `0.0265` n `1227`
- 24h: commodity avg `-0.072` n `13`; crypto_alt avg `0.4797` n `238`; crypto_major avg `0.3007` n `8`; equity avg `0.507` n `156`; fx avg `-0.0306` n `6`; index avg `0.0302` n `27`; metal avg `0.0792` n `20`; unknown avg `3.693` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
