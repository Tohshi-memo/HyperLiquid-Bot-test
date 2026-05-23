# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T19:22:18.624772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1145` n `12`; crypto_alt avg `0.2357` n `228`; crypto_major avg `0.1657` n `8`; equity avg `0.0722` n `67`; fx avg `-0.0006` n `6`; index avg `0.0241` n `23`; metal avg `0.0466` n `18`; unknown avg `0.3644` n `396`
- 1h: commodity avg `-0.5899` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `0.0668` n `8`; equity avg `0.3497` n `67`; fx avg `-0.0015` n `6`; index avg `0.2513` n `23`; metal avg `0.0623` n `18`; unknown avg `0.1393` n `396`
- 4h: commodity avg `-1.0353` n `12`; crypto_alt avg `1.4232` n `228`; crypto_major avg `0.7991` n `8`; equity avg `0.5582` n `67`; fx avg `0.0079` n `6`; index avg `0.2502` n `23`; metal avg `0.1511` n `18`; unknown avg `1.2287` n `396`
- 24h: commodity avg `-0.7636` n `12`; crypto_alt avg `0.3022` n `228`; crypto_major avg `0.129` n `8`; equity avg `0.3892` n `67`; fx avg `-0.0212` n `6`; index avg `0.2172` n `23`; metal avg `0.1771` n `18`; unknown avg `-0.7343` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
