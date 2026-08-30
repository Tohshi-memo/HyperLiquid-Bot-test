# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T11:37:26.877478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0902` n `231`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0038` n `128`; fx avg `0.0002` n `6`; index avg `-0.0068` n `26`; metal avg `0.0047` n `20`; unknown avg `0.0112` n `793`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `0.0177` n `231`; crypto_major avg `0.0428` n `8`; equity avg `0.0294` n `128`; fx avg `0.0023` n `6`; index avg `0.0074` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.0968` n `789`
- 4h: commodity avg `0.0236` n `12`; crypto_alt avg `0.4182` n `231`; crypto_major avg `-0.0189` n `8`; equity avg `0.026` n `128`; fx avg `0.001` n `6`; index avg `0.0045` n `26`; metal avg `0.0034` n `20`; unknown avg `-0.3267` n `789`
- 24h: commodity avg `-0.0175` n `12`; crypto_alt avg `1.4755` n `231`; crypto_major avg `0.8947` n `8`; equity avg `0.2689` n `128`; fx avg `0.0132` n `6`; index avg `0.0671` n `26`; metal avg `0.091` n `20`; unknown avg `0.4057` n `732`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
