# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T07:52:33.448293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0782` n `230`; crypto_major avg `-0.0132` n `8`; equity avg `-0.015` n `100`; fx avg `0.0052` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0802` n `20`; unknown avg `-0.0677` n `775`
- 1h: commodity avg `0.0672` n `12`; crypto_alt avg `-0.1076` n `230`; crypto_major avg `-0.1874` n `8`; equity avg `0.0364` n `100`; fx avg `-0.0421` n `6`; index avg `-0.0014` n `25`; metal avg `0.0372` n `20`; unknown avg `-0.0097` n `775`
- 4h: commodity avg `-0.3518` n `12`; crypto_alt avg `-0.0631` n `230`; crypto_major avg `0.2087` n `8`; equity avg `0.6886` n `100`; fx avg `0.0085` n `6`; index avg `0.138` n `25`; metal avg `0.1391` n `20`; unknown avg `-0.0064` n `759`
- 24h: commodity avg `-0.7573` n `12`; crypto_alt avg `0.7689` n `230`; crypto_major avg `1.4449` n `8`; equity avg `1.3706` n `100`; fx avg `0.0752` n `6`; index avg `0.1675` n `25`; metal avg `0.442` n `20`; unknown avg `-0.0431` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
