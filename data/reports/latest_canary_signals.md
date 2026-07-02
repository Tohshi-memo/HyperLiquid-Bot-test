# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T07:52:44.233588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.2162` n `228`; crypto_major avg `0.1833` n `8`; equity avg `0.1296` n `88`; fx avg `-0.0151` n `6`; index avg `0.0278` n `25`; metal avg `-0.0114` n `20`; unknown avg `0.1617` n `763`
- 1h: commodity avg `0.1076` n `12`; crypto_alt avg `0.2647` n `228`; crypto_major avg `0.1072` n `8`; equity avg `0.0712` n `88`; fx avg `-0.0026` n `6`; index avg `0.0159` n `25`; metal avg `-0.0759` n `20`; unknown avg `0.4414` n `763`
- 4h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.4237` n `228`; crypto_major avg `-0.9364` n `8`; equity avg `-1.1526` n `88`; fx avg `-0.0547` n `6`; index avg `-0.2385` n `25`; metal avg `-0.2213` n `20`; unknown avg `0.1889` n `741`
- 24h: commodity avg `-0.5199` n `12`; crypto_alt avg `2.1804` n `228`; crypto_major avg `1.415` n `8`; equity avg `-2.2181` n `88`; fx avg `-0.078` n `6`; index avg `-0.5459` n `25`; metal avg `1.0664` n `20`; unknown avg `25.2432` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
