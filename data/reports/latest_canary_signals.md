# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T22:52:26.986778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0527` n `230`; crypto_major avg `-0.0205` n `8`; equity avg `0.0249` n `94`; fx avg `-0.005` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0846` n `768`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.1078` n `8`; equity avg `-0.1754` n `94`; fx avg `-0.0111` n `6`; index avg `-0.0237` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.2449` n `768`
- 4h: commodity avg `0.0871` n `12`; crypto_alt avg `0.0836` n `230`; crypto_major avg `-0.0863` n `8`; equity avg `0.0382` n `94`; fx avg `0.0037` n `6`; index avg `0.0259` n `25`; metal avg `-0.0587` n `20`; unknown avg `-0.047` n `768`
- 24h: commodity avg `0.0977` n `12`; crypto_alt avg `0.3283` n `230`; crypto_major avg `0.4913` n `8`; equity avg `-0.7222` n `93`; fx avg `0.2041` n `6`; index avg `-0.1803` n `25`; metal avg `0.1558` n `20`; unknown avg `0.0996` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1231`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1143`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0928`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `669`, weak_sample_signal
