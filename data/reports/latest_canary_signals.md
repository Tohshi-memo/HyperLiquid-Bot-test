# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T20:19:01.384809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0525` n `230`; crypto_major avg `-0.0546` n `8`; equity avg `-0.0325` n `102`; fx avg `0.0063` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.1166` n `774`
- 1h: commodity avg `-0.0841` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `-0.0135` n `8`; equity avg `0.0364` n `102`; fx avg `-0.0038` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0312` n `20`; unknown avg `-0.1669` n `774`
- 4h: commodity avg `-0.3992` n `12`; crypto_alt avg `0.389` n `230`; crypto_major avg `0.3275` n `8`; equity avg `0.9586` n `102`; fx avg `-0.0323` n `6`; index avg `0.1545` n `25`; metal avg `-0.045` n `20`; unknown avg `95.7982` n `774`
- 24h: commodity avg `-1.0515` n `12`; crypto_alt avg `-0.9485` n `230`; crypto_major avg `-0.2652` n `8`; equity avg `-1.0111` n `102`; fx avg `-0.0324` n `6`; index avg `-0.3289` n `25`; metal avg `0.2165` n `20`; unknown avg `97.7036` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
