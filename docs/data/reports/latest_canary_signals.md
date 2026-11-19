# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T04:37:28.766221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0298` n `13`; crypto_alt avg `0.0585` n `239`; crypto_major avg `0.0593` n `8`; equity avg `-0.1833` n `164`; fx avg `0.0028` n `6`; index avg `-0.0333` n `27`; metal avg `-0.0182` n `20`; unknown avg `39.8489` n `1264`
- 1h: commodity avg `0.109` n `13`; crypto_alt avg `0.6549` n `239`; crypto_major avg `0.9081` n `8`; equity avg `0.4193` n `164`; fx avg `0.0347` n `6`; index avg `0.0755` n `27`; metal avg `0.1695` n `20`; unknown avg `13.3264` n `1244`
- 4h: commodity avg `0.088` n `13`; crypto_alt avg `0.6827` n `239`; crypto_major avg `0.6536` n `8`; equity avg `0.0033` n `164`; fx avg `0.0258` n `6`; index avg `0.0257` n `27`; metal avg `-0.214` n `20`; unknown avg `3.3668` n `1239`
- 24h: commodity avg `0.1045` n `13`; crypto_alt avg `0.645` n `239`; crypto_major avg `-0.6966` n `8`; equity avg `-0.1793` n `164`; fx avg `-0.0882` n `6`; index avg `0.084` n `27`; metal avg `-0.5251` n `20`; unknown avg `252.8876` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
