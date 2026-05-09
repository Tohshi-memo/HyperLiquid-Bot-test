# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T01:37:15.549922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.2915` n `228`; crypto_major avg `0.2928` n `8`; equity avg `-0.0305` n `65`; fx avg `0.0204` n `5`; index avg `-0.0015` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.2648` n `375`
- 1h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.6491` n `228`; crypto_major avg `0.47` n `8`; equity avg `0.0122` n `65`; fx avg `0.0123` n `5`; index avg `-0.0353` n `23`; metal avg `0.1416` n `18`; unknown avg `-0.0866` n `375`
- 4h: commodity avg `-0.2651` n `12`; crypto_alt avg `1.2826` n `228`; crypto_major avg `0.6987` n `8`; equity avg `0.1337` n `65`; fx avg `0.0021` n `5`; index avg `0.1118` n `23`; metal avg `-0.0945` n `18`; unknown avg `-0.303` n `375`
- 24h: commodity avg `-0.5528` n `12`; crypto_alt avg `4.8541` n `228`; crypto_major avg `2.6199` n `8`; equity avg `3.6388` n `65`; fx avg `0.1083` n `5`; index avg `1.2556` n `23`; metal avg `0.3132` n `18`; unknown avg `1.1991` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
