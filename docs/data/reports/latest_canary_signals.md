# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T01:38:05.522206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0036` n `231`; crypto_major avg `-0.0599` n `8`; equity avg `0.0023` n `128`; fx avg `-0.0006` n `6`; index avg `0.0167` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.0262` n `793`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.2802` n `231`; crypto_major avg `-0.2467` n `8`; equity avg `-0.0027` n `128`; fx avg `0.0002` n `6`; index avg `0.0115` n `26`; metal avg `0.0058` n `20`; unknown avg `0.054` n `793`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `-0.183` n `231`; crypto_major avg `-0.0613` n `8`; equity avg `0.0241` n `128`; fx avg `0.0201` n `6`; index avg `0.0349` n `26`; metal avg `-0.0028` n `20`; unknown avg `4.3387` n `774`
- 24h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.051` n `231`; crypto_major avg `0.679` n `8`; equity avg `0.4012` n `128`; fx avg `-0.013` n `6`; index avg `0.114` n `26`; metal avg `0.1279` n `20`; unknown avg `0.0018` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2292`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
