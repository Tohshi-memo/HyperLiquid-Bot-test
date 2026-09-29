# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T15:52:38.222063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5507` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4951` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3719` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0914` n `12`; crypto_alt avg `-0.2066` n `234`; crypto_major avg `-0.2284` n `8`; equity avg `-0.0465` n `141`; fx avg `-0.0107` n `6`; index avg `-0.0093` n `26`; metal avg `0.0034` n `20`; unknown avg `6.645` n `963`
- 1h: commodity avg `-0.0401` n `12`; crypto_alt avg `-1.667` n `234`; crypto_major avg `-1.4832` n `8`; equity avg `-0.5449` n `141`; fx avg `-0.0211` n `6`; index avg `-0.1113` n `26`; metal avg `-0.1065` n `20`; unknown avg `2.9507` n `931`
- 4h: commodity avg `-0.1586` n `12`; crypto_alt avg `-1.4765` n `234`; crypto_major avg `-1.5913` n `8`; equity avg `-0.0406` n `141`; fx avg `-0.0213` n `6`; index avg `-0.0962` n `26`; metal avg `-0.1839` n `20`; unknown avg `4.4769` n `893`
- 24h: commodity avg `-0.8807` n `12`; crypto_alt avg `1.493` n `234`; crypto_major avg `-0.229` n `8`; equity avg `1.0641` n `141`; fx avg `-0.1508` n `6`; index avg `0.0827` n `26`; metal avg `-0.0208` n `20`; unknown avg `15.9788` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
