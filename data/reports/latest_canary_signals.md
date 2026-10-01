# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T07:37:32.731553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `13`; crypto_alt avg `-0.3055` n `234`; crypto_major avg `-0.1875` n `8`; equity avg `-0.2128` n `142`; fx avg `-0.0194` n `6`; index avg `-0.0407` n `26`; metal avg `-0.0564` n `20`; unknown avg `0.2872` n `975`
- 1h: commodity avg `0.4035` n `13`; crypto_alt avg `-0.8934` n `234`; crypto_major avg `-0.8123` n `8`; equity avg `-0.7115` n `142`; fx avg `0.0168` n `6`; index avg `-0.1788` n `26`; metal avg `-0.2546` n `20`; unknown avg `3.1725` n `972`
- 4h: commodity avg `0.553` n `13`; crypto_alt avg `-0.5994` n `234`; crypto_major avg `-0.2467` n `8`; equity avg `-0.0059` n `142`; fx avg `-0.0075` n `6`; index avg `-0.0323` n `26`; metal avg `-0.1286` n `20`; unknown avg `0.4436` n `940`
- 24h: commodity avg `0.3126` n `13`; crypto_alt avg `0.4709` n `234`; crypto_major avg `0.5416` n `8`; equity avg `0.202` n `142`; fx avg `0.1866` n `6`; index avg `0.0476` n `26`; metal avg `-0.4276` n `20`; unknown avg `774.7711` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
