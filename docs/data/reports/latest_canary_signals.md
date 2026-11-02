# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T23:52:28.959545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.0179` n `239`; crypto_major avg `-0.0253` n `8`; equity avg `-0.1329` n `157`; fx avg `0.017` n `6`; index avg `-0.0287` n `27`; metal avg `0.0068` n `20`; unknown avg `-0.2675` n `1264`
- 1h: commodity avg `-0.0426` n `13`; crypto_alt avg `-0.0624` n `239`; crypto_major avg `-0.1188` n `8`; equity avg `0.2237` n `157`; fx avg `0.0099` n `6`; index avg `0.0728` n `27`; metal avg `-0.0181` n `20`; unknown avg `-0.3562` n `1250`
- 4h: commodity avg `-0.0827` n `13`; crypto_alt avg `0.6254` n `239`; crypto_major avg `0.3586` n `8`; equity avg `0.1431` n `157`; fx avg `0.0036` n `6`; index avg `0.0138` n `27`; metal avg `0.0216` n `20`; unknown avg `13.8545` n `1144`
- 24h: commodity avg `-1.358` n `13`; crypto_alt avg `-2.9171` n `238`; crypto_major avg `-1.7873` n `8`; equity avg `-2.912` n `157`; fx avg `0.2708` n `6`; index avg `0.001` n `27`; metal avg `0.0663` n `20`; unknown avg `12.6469` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
