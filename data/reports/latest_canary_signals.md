# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T18:52:29.061358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0792` n `12`; crypto_alt avg `0.0074` n `228`; crypto_major avg `-0.0071` n `8`; equity avg `0.0295` n `78`; fx avg `0.0` n `6`; index avg `0.0056` n `23`; metal avg `0.0001` n `18`; unknown avg `0.0432` n `702`
- 1h: commodity avg `0.1138` n `12`; crypto_alt avg `0.0165` n `228`; crypto_major avg `0.1423` n `8`; equity avg `-0.0038` n `78`; fx avg `0.0033` n `6`; index avg `-0.0102` n `23`; metal avg `-0.0874` n `18`; unknown avg `0.2375` n `702`
- 4h: commodity avg `0.2451` n `12`; crypto_alt avg `0.0835` n `228`; crypto_major avg `0.2237` n `8`; equity avg `0.0395` n `78`; fx avg `-0.0237` n `6`; index avg `-0.0166` n `23`; metal avg `-0.0672` n `18`; unknown avg `-0.4321` n `702`
- 24h: commodity avg `0.3003` n `12`; crypto_alt avg `1.5213` n `228`; crypto_major avg `0.4642` n `8`; equity avg `0.449` n `78`; fx avg `-0.0694` n `6`; index avg `0.014` n `23`; metal avg `-0.0945` n `18`; unknown avg `-0.2089` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
