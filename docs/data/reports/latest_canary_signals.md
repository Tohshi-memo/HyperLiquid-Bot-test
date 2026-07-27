# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T02:07:36.828237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `0.0211` n `230`; crypto_major avg `0.0689` n `8`; equity avg `0.1531` n `100`; fx avg `-0.0012` n `6`; index avg `0.0033` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.078` n `775`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `0.0292` n `230`; crypto_major avg `-0.0556` n `8`; equity avg `-0.1719` n `100`; fx avg `0.0241` n `6`; index avg `-0.0531` n `25`; metal avg `0.0463` n `20`; unknown avg `-0.1` n `775`
- 4h: commodity avg `0.1644` n `12`; crypto_alt avg `0.152` n `230`; crypto_major avg `0.066` n `8`; equity avg `-0.249` n `100`; fx avg `0.0919` n `6`; index avg `-0.1212` n `25`; metal avg `0.0711` n `20`; unknown avg `-0.4248` n `775`
- 24h: commodity avg `-0.4962` n `12`; crypto_alt avg `1.5706` n `230`; crypto_major avg `1.464` n `8`; equity avg `0.5301` n `100`; fx avg `0.1409` n `6`; index avg `0.0311` n `25`; metal avg `0.4661` n `20`; unknown avg `0.0329` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
