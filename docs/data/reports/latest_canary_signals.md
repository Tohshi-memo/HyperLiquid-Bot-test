# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T22:37:28.586200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `13`; crypto_alt avg `-0.0393` n `238`; crypto_major avg `0.1322` n `8`; equity avg `0.0172` n `156`; fx avg `-0.0056` n `6`; index avg `0.0086` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.0187` n `1261`
- 1h: commodity avg `0.0225` n `13`; crypto_alt avg `-0.5085` n `238`; crypto_major avg `-0.5138` n `8`; equity avg `-0.1286` n `156`; fx avg `0.0265` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0167` n `20`; unknown avg `9.2722` n `1245`
- 4h: commodity avg `0.0681` n `13`; crypto_alt avg `-0.6605` n `238`; crypto_major avg `-0.5518` n `8`; equity avg `-0.0891` n `156`; fx avg `-0.0263` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0453` n `20`; unknown avg `13.3995` n `1203`
- 24h: commodity avg `0.0134` n `13`; crypto_alt avg `-1.0001` n `238`; crypto_major avg `-0.6067` n `8`; equity avg `0.2136` n `156`; fx avg `-0.0089` n `6`; index avg `0.0483` n `27`; metal avg `0.0061` n `20`; unknown avg `3.6228` n `1094`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
