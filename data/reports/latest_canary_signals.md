# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T01:07:26.862543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0277` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.214` n `12`; crypto_alt avg `0.2682` n `228`; crypto_major avg `0.1274` n `8`; equity avg `0.2017` n `74`; fx avg `-0.0056` n `6`; index avg `0.0332` n `23`; metal avg `-0.4999` n `18`; unknown avg `0.4451` n `547`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `-0.0892` n `228`; crypto_major avg `-0.4696` n `8`; equity avg `-0.3609` n `74`; fx avg `-0.0163` n `6`; index avg `-0.1774` n `23`; metal avg `-0.9417` n `18`; unknown avg `-0.0871` n `547`
- 4h: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.6195` n `228`; crypto_major avg `-1.1756` n `8`; equity avg `-0.3292` n `74`; fx avg `-0.0586` n `6`; index avg `-0.1479` n `23`; metal avg `-1.488` n `18`; unknown avg `-0.3875` n `547`
- 24h: commodity avg `-0.6825` n `12`; crypto_alt avg `0.4848` n `228`; crypto_major avg `-1.7841` n `8`; equity avg `-1.4936` n `74`; fx avg `0.0545` n `6`; index avg `-0.6022` n `23`; metal avg `-2.6348` n `18`; unknown avg `-0.3197` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0374`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0322`, n `668`, weak_sample_signal
